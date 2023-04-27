import React from "react";


function Category(props) {

    const { category, handleCategoryClick, activeCat } = props;
    
    

    return (
        <>
        <ul class="nav nav-tabs nav-tabs-fill" role="tablist">


            {!activeCat ? 
                <li class="nav-item">
                    <a href="/#" class="nav-link active" role="tab" data-toggle="tab">All</a>
                </li>
            :
                <li class="nav-item">
                    <a href="/#" onClick={() => handleCategoryClick(null)} class="nav-link" role="tab" data-toggle="tab">All</a>
                </li>
            }

            {category.map((cat) => (
                <div key={cat.category_id}>
                {cat.category_id === activeCat ?
                    <li  class="nav-item">
                        <a href="/#" class="nav-link active" role="tab" data-toggle="tab">{cat.name}</a>
                    </li>
                :
                    <li class="nav-item">
                        <a href="/#" onClick={() => handleCategoryClick(cat.category_id)} class="nav-link" role="tab" data-toggle="tab">{cat.name}</a>
                    </li>
                }
                </div>
            ))} 
        </ul>
        </>
    );
}

export default Category;
